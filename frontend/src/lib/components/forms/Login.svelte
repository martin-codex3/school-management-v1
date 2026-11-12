<script lang="ts">
    import StyledButton from "#lib/components/buttons/StyledButton.svelte";
    import TextInput from "#lib/components/inputs/TextInput.svelte";
    import { enhance } from "$app/forms";
    import { toast } from "svelte-sonner";
    import type { ActionData } from "../../../routes/$types";

    let isCreatingAccount: boolean = $state(false);

    interface Props {
        form: ActionData;
    }
    const { form }: Props = $props();

    let errorTitle: string = $state("");

    $effect(() => {
        if (form?.problem?.title) {
            errorTitle = form?.problem?.title;
        }

        if (form?.problem?.detail) {
            errorTitle = form?.problem?.detail;
        }
    });

    const fieldErrors = $derived((field: any) => {
        return form?.problem?.errors?.find((error) => error.pointer === field);
    });
</script>

<div
    class="translate-y-10 h-full motion-preset-slide-down-sm motion-duration-200 px-20 space-y-10"
>
    <div>
        <h1 class="text-4xl capitalize font-bold">welcome</h1>
        <p class="text-lg text-gray-500">Log in to access your account</p>
    </div>
    <form
        action="?/createAccount"
        method="POST"
        use:enhance={() => {
            isCreatingAccount = true;
            return async ({ update, result }) => {
                await update();
                isCreatingAccount = false;

                if (result.type === "failure") {
                    toast.error(errorTitle);
                }

                if (result.type === "error") {
                    console.log("there will be an error here");
                }
            };
        }}
    >
        <div class="input__wrapper space-y-8">
            <div>
                <button
                    aria-label="google authenticaion"
                    title="Continue With Google"
                    class="w-full bg-gray-100 border border-gray-300 cursor-pointer rounded-full py-2 flex items-center justify-center"
                >
                    <span class="first-letter:capitalize font-semibold"
                        >continue with google</span
                    >
                </button>
            </div>
            <div class="space-y-5">
                <TextInput
                    type="text"
                    name="first_name"
                    placeholder="John"
                    id="FirstName"
                    label="First name"
                    valueError=""
                />

                <TextInput
                    type="text"
                    name="first_name"
                    placeholder="John"
                    id="FirstName"
                    label="First name"
                    valueError=""
                />

                <StyledButton
                    title="Create Account"
                    label="create account"
                    isLoading={isCreatingAccount}
                />
            </div>
        </div>
    </form>
</div>
