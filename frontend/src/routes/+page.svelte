<script lang="ts">
    import StyledButton from "#lib/components/buttons/StyledButton.svelte";
    import SelectInput from "#lib/components/inputs/SelectInput.svelte";
    import SelectInpu from "#lib/components/inputs/SelectInput.svelte";
    import TextInput from "#lib/components/inputs/TextInput.svelte";
    import { enhance } from "$app/forms";
    import NumberIcon from "@iconify-svelte/tabler/number-1";
    import NumberIcon2 from "@iconify-svelte/tabler/number-2";
    import type { PageProps } from "./$types";
    import { toast } from "svelte-sonner";
    import { getCountryDataList } from "countries-list";

    let isCreatingAccount: boolean = $state(false);

    const { form }: PageProps = $props();
    let errorTitle: string = $state("");

    $effect(() => {
        if (form?.problem) {
            errorTitle = form?.problem?.title;
        }
    });

    const fieldErrors = $derived((field: any) => {
        return form?.problem?.errors?.find((error) => error.pointer === field);
    });
</script>

<section class="h-screen flex items-center justify-center px-5 lg:px-0">
    <div
        class="bg-white rounded-4xl w-full border border-primary-border py-5 px-5 max-w-3xl h-[calc(100vh-3rem)] mx-auto"
    >
        <div class="h-full overflow-auto scrollbar-thin px-5 space-y-10 py-5">
            <div class="flex items-center justify-center gap-5">
                <button
                    aria-label="options button"
                    title="Sign In"
                    class="flex items-center justify-center p-3 rounded-full border cursor-pointer transition duration-200 hover:outline-1 outline-primary-main-purple text-primary-main-purple"
                >
                    <NumberIcon height="1.5em" class="shrink-0" />
                </button>

                <button
                    aria-label="options button"
                    title="Sign In"
                    class="flex items-center justify-center p-3 rounded-full border cursor-pointer transition duration-200 hover:outline-1 outline-primary-main-purple text-primary-main-purple"
                >
                    <NumberIcon height="1.5em" class="shrink-0" />
                </button>
            </div>

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
                    <div class="wrapper space-y-5">
                        <div
                            class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-5"
                        >
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

                        <div
                            class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-5"
                        >
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
                                valueError={fieldErrors("#/phone_number")
                                    ?.detail}
                            />
                        </div>

                        <div
                            class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-5"
                        >
                            <TextInput
                                type="text"
                                name="school_name"
                                placeholder=""
                                id="SchoolName"
                                label="School name"
                                valueError={fieldErrors("#/school_name")
                                    ?.detail}
                            />

                            <SelectInput
                                name="school_type"
                                id="SchoolType"
                                placeholder=""
                                label="School type"
                                fieldError={fieldErrors("#/school_type")
                                    ?.detail}
                            >
                                <option value="">Select option</option>
                                <option value="Primary School"
                                    >Primary School</option
                                >
                                <option value="Secondary School"
                                    >Secondary School</option
                                >
                                <option value="Combined School"
                                    >Combined School</option
                                >
                                <option value="International School"
                                    >International School</option
                                >
                                <option value="Other">Other</option>
                            </SelectInput>
                        </div>

                        <div
                            class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-5"
                        >
                            <TextInput
                                type="email"
                                name="school_email"
                                placeholder="school@example.com"
                                id="SchoolEmail"
                                label="School email"
                                valueError={fieldErrors("#/school_email")
                                    ?.detail}
                            />

                            <TextInput
                                type="text"
                                name="school_phone"
                                placeholder=""
                                id="SchoolPhone"
                                label="School phone"
                                valueError={fieldErrors("#/school_phone")
                                    ?.detail}
                            />
                        </div>

                        <div
                            class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-5"
                        >
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

                        <div
                            class="grid grid-cols-1 md:grid-cols-1 lg:grid-cols-1 gap-5"
                        >
                            <SelectInput
                                name="country"
                                placeholder="Malawi"
                                id="Country"
                                label="Country"
                                fieldError={fieldErrors("#/country")?.detail}
                            >
                                <option value="">Selection option</option>
                                {#each getCountryDataList() as country}
                                    <option value={country.name}
                                        >{country.name}</option
                                    >
                                {/each}
                            </SelectInput>
                        </div>

                        <div
                            class="grid grid-cols-1 md:grid-cols-1 lg:grid-cols-1 gap-5"
                        >
                            <TextInput
                                type="password"
                                name="password_hash"
                                placeholder=""
                                id="Password"
                                label="Password"
                                valueError={fieldErrors("#/password_hash")
                                    ?.detail}
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
        </div>
    </div>
</section>
