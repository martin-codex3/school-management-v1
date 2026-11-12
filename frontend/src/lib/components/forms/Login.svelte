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

<div>
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
        <div class="input__wrapper">
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
    </form>
</div>
