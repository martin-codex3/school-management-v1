<script lang="ts">
    import StyledButton from "#lib/components/buttons/StyledButton.svelte";
    import SelectInput from "#lib/components/inputs/SelectInput.svelte";
    import TextInput from "#lib/components/inputs/TextInput.svelte";
    import { enhance } from "$app/forms";
    import { toast } from "svelte-sonner";
    import { getCountryDataList } from "countries-list";
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
    class="motion-preset-slide-down-sm motion-duration-300 px-0 md:px-10 lg:px-14 space-y-10"
>
    <div>
        <h1 class="text-4xl capitalize font-bold">Create your account.</h1>
        <p class="text-lg text-gray-500">
            Create your account to get access to all the features
        </p>
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
                    toast.error(errorTitle);
                }

                if (result.type === "success") {
                    toast.success(
                        "Account created successfully. You'll get redirected to the dashboard",
                    );
                }
            };
        }}
    >
        <div class="wrapper space-y-5">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-5">
                <TextInput
                    type="text"
                    name="first_name"
                    placeholder="John"
                    id="FirstName"
                    label="First name"
                    valueError={fieldErrors("#/first_name")?.detail}
                />

                <TextInput
                    type="text"
                    name="last_name"
                    placeholder="Doe"
                    id="LastName"
                    label="Last name"
                    valueError={fieldErrors("#/last_name")?.detail}
                />
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-5">
                <TextInput
                    type="email"
                    name="email"
                    placeholder="user@example.com"
                    id="Email"
                    label="Email"
                    valueError={fieldErrors("#/email")?.detail}
                />

                <TextInput
                    type="text"
                    name="phone_number"
                    placeholder=""
                    id="PhoneNumber"
                    label="Phone number"
                    valueError={fieldErrors("#/phone_number")?.detail}
                />
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-5">
                <TextInput
                    type="text"
                    name="school_name"
                    placeholder=""
                    id="SchoolName"
                    label="School name"
                    valueError={fieldErrors("#/school_name")?.detail}
                />

                <SelectInput
                    name="school_type"
                    id="SchoolType"
                    placeholder=""
                    label="School type"
                    fieldError={fieldErrors("#/school_type")?.detail}
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
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-5">
                <TextInput
                    type="email"
                    name="school_email"
                    placeholder="school@example.com"
                    id="SchoolEmail"
                    label="School email"
                    valueError={fieldErrors("#/school_email")?.detail}
                />

                <TextInput
                    type="text"
                    name="school_phone"
                    placeholder=""
                    id="SchoolPhone"
                    label="School phone"
                    valueError={fieldErrors("#/school_phone")?.detail}
                />
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-5">
                <TextInput
                    type="text"
                    name="address"
                    placeholder=""
                    id="Address"
                    label="Address"
                    valueError={fieldErrors("#/address")?.detail}
                />

                <TextInput
                    type="text"
                    name="city"
                    placeholder="Blantyre"
                    id="City"
                    label="City"
                    valueError={fieldErrors("#/city")?.detail}
                />
            </div>

            <div class="grid grid-cols-1 md:grid-cols-1 lg:grid-cols-1 gap-5">
                <SelectInput
                    name="country"
                    placeholder="Malawi"
                    id="Country"
                    label="Country"
                    fieldError={fieldErrors("#/country")?.detail}
                >
                    <option value="">Selection option</option>
                    {#each getCountryDataList() as country}
                        <option value={country.name}>{country.name}</option>
                    {/each}
                </SelectInput>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-1 lg:grid-cols-1 gap-5">
                <TextInput
                    type="password"
                    name="password_hash"
                    placeholder=""
                    id="Password"
                    label="Password"
                    valueError={fieldErrors("#/password_hash")?.detail}
                />
            </div>

            <StyledButton
                title="Create Account"
                label="create account"
                isLoading={isCreatingAccount}
            />
        </div>
    </form>
</div>
