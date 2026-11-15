<script lang="ts">
    import StyledButton from "#lib/components/buttons/StyledButton.svelte";
    import TextInput from "#lib/components/inputs/TextInput.svelte";
    import { enhance } from "$app/forms";
    import CloseIcon from "@iconify-svelte/material-symbols/close";
    import { toast } from "svelte-sonner";
    import type { ActionData } from "../../../../routes/$types";

    interface Props {
        toggleModal: boolean;
        closeModal: () => void;
        name: string;
        label: string;
        fieldValue: string;
        form: ActionData;
    }

    let { closeModal, toggleModal, name, label, fieldValue, form }: Props =
        $props();

    let isUpdatingProfile: boolean = $state(false);
    let errorTitle: string = $state("");

    $effect(() => {
        if (form?.problem) {
            errorTitle = form.problem.title;
        }

        if (form?.problem?.detail) {
            errorTitle = form.problem.detail;
        }
    });

    // for the returned form errors here
    const fieldError = $derived((field: string) => {
        return form?.problem?.errors.find((e) => e.pointer === field);
    });
</script>

{#snippet formInput()}
    <form
        action="?/updateProfile"
        method="POST"
        use:enhance={() => {
            isUpdatingProfile = false;
            return async ({ result, update }) => {
                if (result.type === "failure") {
                    toast.error("Error man");
                }

                if (result.type === "error") {
                    toast.error(errorTitle);
                }

                if (result.type === "success") {
                    toast.success(errorTitle);
                }
            };
        }}
    >
        <div class="space-y-7">
            <TextInput
                type="text"
                {name}
                placeholder=""
                id={label}
                {label}
                valueError=""
                value={fieldValue}
            />

            <StyledButton
                label="Update detail"
                isLoading={isUpdatingProfile}
                title="Update Detail"
            />
        </div>
    </form>
{/snippet}

<div
    class="fixed bg-black/20 backdrop-blur-sm flex items-center justify-center inset-0 z-100"
>
    <div
        class={[
            "bg-white rounded-4xl border border-black/30 w-lg h-fit px-10 py-5 space-y-5",
            toggleModal
                ? "motion-preset-slide-down-sm motion-duration-200"
                : "motion-translate-y-out-150 motion-duration-300",
        ]}
    >
        <!-- for the header -->
        <div class="flex items-center justify-between">
            <h1 class="text-2xl first-letter:capitalize font-bold">
                Update detail
            </h1>
            <button
                aria-label="close button"
                title="Close Modal"
                onclick={closeModal}
                class="flex items-center justify-center p-2 cursor-pointer hover:bg-purple-100 rounded-full transition duration-200"
            >
                <CloseIcon height="1.5em" class="shrink-0" />
            </button>
        </div>

        <div>
            <p>
                Make changes to your profile details. The changes will be synced
                automatically
            </p>
        </div>

        {@render formInput()}
    </div>
</div>
