<script lang="ts">
    import StyledButton from "#lib/components/buttons/StyledButton.svelte";
    import TextInput from "#lib/components/inputs/TextInput.svelte";
    import { enhance } from "$app/forms";
    import { toast } from "svelte-sonner";
    import type { ActionData } from "../../../routes/$types";
    import GoogleIcon from "@iconify-svelte/devicon/google";

    let isSigningIn: boolean = $state(false);

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
        action="?/loginUser"
        method="POST"
        use:enhance={() => {
            isSigningIn = true;
            return async ({ update, result }) => {
                await update();
                isSigningIn = false;

                if (result.type === "failure") {
                    toast.error(errorTitle);
                }

                if (result.type === "error") {
                    toast.error(errorTitle);
                }

                if (result.type === "success") {
                    toast.success("Logged in successfully");
                }
            };
        }}
    >
        <div class="input__wrapper space-y-8">
            <div>
                <button
                    aria-label="google authenticaion"
                    title="Continue With Google"
                    class="w-full bg-gray-100 border border-gray-300 cursor-pointer rounded-full py-2 flex items-center justify-center gap-3"
                >
                    <GoogleIcon height="1.5em" class="shrink-0" />
                    <span class="first-letter:capitalize font-semibold"
                        >continue with google</span
                    >
                </button>
            </div>
            <div class="space-y-5">
                <TextInput
                    type="email"
                    name="username"
                    placeholder="user@example.com"
                    id="Email"
                    label="Email"
                    valueError=""
                />

                <TextInput
                    type="password"
                    name="password_hash"
                    placeholder=""
                    id="Password"
                    label="Password"
                    valueError=""
                />

                <StyledButton
                    title="Log In"
                    label="Log in"
                    isLoading={isSigningIn}
                />
            </div>
        </div>
    </form>
</div>
