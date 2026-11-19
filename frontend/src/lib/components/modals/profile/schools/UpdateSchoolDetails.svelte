<script lang="ts">
    import StyledButton from "#lib/components/buttons/StyledButton.svelte";
    import TextInput from "#lib/components/inputs/TextInput.svelte";
    import { enhance } from "$app/forms";
    import CloseIcon from "@iconify-svelte/material-symbols/close";
    import { toast } from "svelte-sonner";
    import TextAreaInput from "#lib/components/inputs/TextAreaInput.svelte";
    import type { ActionData } from "../../../../../routes/$types";
    import SelectInput from "#lib/components/inputs/SelectInput.svelte";

    interface Props {
        toggleModal: boolean;
        closeModal: () => void;
        name: string;
        label: string;
        fieldValue: string | boolean | undefined | object;
        form: ActionData;
    }

    let { closeModal, toggleModal, name, label, fieldValue, form }: Props =
        $props();

    let isUpdatingProfile: boolean = $state(false);
    let errorTitle: string = $state("");

    $effect(() => {
        if (form?.problem?.title) {
            errorTitle = form?.problem?.title;
        }

        if (form?.problem?.detail) {
            errorTitle = form?.problem?.detail;
        }
    });

    // for the returned form errors here
    const fieldError = $derived((field: string) => {
        return form?.problem?.errors?.find((e) => e.pointer === field);
    });
</script>

{#snippet formInput()}
    <form
        action="?/updateSchoolDetails"
        method="POST"
        use:enhance={() => {
            isUpdatingProfile = true;
            return async ({ result, update }) => {
                await update({
                    reset: false,
                    refreshAll: true,
                    invalidateAll: true,
                });
                isUpdatingProfile = false;

                // we will update the states here
                if (result.type === "failure") {
                    toast.error(errorTitle);
                }

                if (result.type === "error") {
                    toast.error(errorTitle);
                }

                if (result.type === "success") {
                    toast.success("Updated successfully");
                }
            };
        }}
    >
        <div class="space-y-7">
            {#if name === "email"}
                <div class="bg-green-200 text-green-950 px-4 py-2 rounded-lg">
                    <p class="first-letter:uppercase">
                        once you chage your email, the changes will be reflected
                        the next time you try to login.
                    </p>
                </div>
                <TextInput
                    type="email"
                    {name}
                    placeholder=""
                    id={label}
                    {label}
                    valueError={fieldError(`#/${name}`)?.detail}
                    value={fieldValue}
                />
            {:else if name === "bio"}
                <TextAreaInput
                    {name}
                    placeholder=""
                    id={label}
                    {label}
                    valueError={fieldError(`#/${name}`)?.detail}
                    value={`${fieldValue}`}
                />
            {:else if name === "school_type"}
                <SelectInput
                    {name}
                    placeholder=""
                    id={label}
                    {label}
                    fieldError={fieldError(`#/${name}`)?.detail}
                    value={`${fieldValue}`}
                >
                    <option value="">Select option</option>
                    <option value="Primary School">Primary School</option>
                    <option value="Secondary School">Secondary School</option>
                    <option value="Combined School">Combined School</option>
                    <option value="International School"
                        >International School</option
                    >
                    <option value="Other">Other</option>
                </SelectInput>
            {:else}
                <TextInput
                    type="text"
                    {name}
                    placeholder=""
                    id={label}
                    {label}
                    valueError={fieldError(`#/${name}`)?.detail}
                    value={fieldValue}
                />
            {/if}

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
            "bg-white rounded-4xl border border-black/30 w-lg h-fit px-10 py-7 space-y-5",
            toggleModal
                ? "motion-preset-slide-down-sm motion-duration-200"
                : "motion-translate-y-out-150 motion-duration-300",
        ]}
    >
        <!-- for the header -->
        <div class="flex items-center justify-between">
            <h1 class="text-3xl first-letter:capitalize font-bold">
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
            <p class="text-lg text-gray-400">
                Make changes to your profile details. The changes will be synced
                automatically
            </p>
        </div>

        {@render formInput()}
    </div>
</div>
