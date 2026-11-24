<script lang="ts">
    import StyledButton from "#lib/components/buttons/StyledButton.svelte";
    import SelectInput from "#lib/components/inputs/SelectInput.svelte";
    import TextInput from "#lib/components/inputs/TextInput.svelte";
    import { enhance } from "$app/forms";
    import { getCountryDataList } from "countries-list";
    import { toast } from "svelte-sonner";
    import type { PageProps } from "./$types";

    let isSavingBranch: boolean = $state(false);

    let { form }: PageProps = $props();

    let errorTitle: string = $state("");

    $effect(() => {
        if (form?.problem?.title) {
            errorTitle = form?.problem?.title;
        }

        if (form?.problem?.detail) {
            errorTitle = form?.problem?.detail;
        }
    });

    const fieldErrors = $derived((field: string) => {
        return form?.problem?.errors?.find((e) => field === e.pointer);
    });
</script>

<div class="h-screen overflow-hidden flex items-center justify-center">
    <div
        class="h-[calc(100vh-1rem)] bg-white w-full px-5 border py-5 border-gray-300 rounded-4xl"
    >
        <!-- for the main header -->
        <div class="h-full scrollbar-thin overflow-auto px-5 space-y-10">
            <div>
                <h1 class="text-2xl font-semibold capitalize">create branch</h1>
            </div>

            <!-- for the main form here -->
            <div>
                <form
                    action="?/createBranch"
                    method="POST"
                    use:enhance={() => {
                        isSavingBranch = true;
                        return async ({ result, update }) => {
                            await update({ reset: false, refreshAll: true });
                            isSavingBranch = false;

                            if (result.type === "failure") {
                                toast.error(errorTitle);
                            }

                            if (result.type === "error") {
                                toast.error(errorTitle);
                            }

                            if (result.type === "success") {
                                toast.success("Success");
                            }
                        };
                    }}
                >
                    <div class="form__input__wrapper space-y-7">
                        <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                            <TextInput
                                type="text"
                                id="BranchName"
                                label="Branch name"
                                placeholder=""
                                value=""
                                valueError={fieldErrors("#/branch_name")
                                    ?.detail}
                                name="branch_name"
                            />

                            <TextInput
                                type="email"
                                id="BranchEmail"
                                label="Branch email"
                                placeholder="branch@example.com"
                                value=""
                                valueError={fieldErrors("#/branch_email")
                                    ?.detail}
                                name="branch_email"
                            />
                        </div>

                        <!-- for the phones -->
                        <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                            <TextInput
                                type="text"
                                id="BranchPhone"
                                label="Branch phone"
                                placeholder=""
                                value=""
                                valueError={fieldErrors("#/branch_phone")
                                    ?.detail}
                                name="branch_phone"
                            />

                            <TextInput
                                type="text"
                                id="AlternativePhone"
                                label="Alternative phone"
                                placeholder=""
                                value=""
                                valueError={fieldErrors("#/alternative_phone")
                                    ?.detail}
                                name="alternative_phone"
                            />
                        </div>

                        <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                            <TextInput
                                type="text"
                                id="AddressLine1"
                                label="Address line 1"
                                placeholder=""
                                value=""
                                valueError={fieldErrors("#/address_line_1")
                                    ?.detail}
                                name="address_line_1"
                            />

                            <TextInput
                                type="text"
                                id="AddressLine2"
                                label="Address line 2"
                                placeholder=""
                                value=""
                                valueError={fieldErrors("#/address_line_2")
                                    ?.detail}
                                name="address_line_2"
                            />
                        </div>

                        <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                            <TextInput
                                type="text"
                                id="City"
                                label="City"
                                placeholder="Blantyre"
                                value=""
                                valueError={fieldErrors("#/city")?.detail}
                                name="city"
                            />

                            <SelectInput
                                id="Nationality"
                                label="Nationality"
                                placeholder=""
                                fieldError={fieldErrors("#/nationality")
                                    ?.detail}
                                name="nationality"
                            >
                                <option value="">Select option</option>
                                {#each getCountryDataList() as countries}
                                    <option value={countries.name}
                                        >{countries.name}</option
                                    >
                                {/each}
                            </SelectInput>
                        </div>

                        <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                            <TextInput
                                type="text"
                                id="District"
                                label="District"
                                placeholder=""
                                value=""
                                valueError={fieldErrors("#/district")?.detail}
                                name="district"
                            />

                            <SelectInput
                                id="MainBranch"
                                label="Main branch"
                                placeholder=""
                                fieldError={fieldErrors("#/is_main_branch")
                                    ?.detail}
                                name="is_main_branch"
                            >
                                <option value="">Select option</option>
                                <option value="Yes">Yes</option>
                                <option value="No">No</option>
                            </SelectInput>
                        </div>

                        <StyledButton
                            isLoading={isSavingBranch}
                            label="Save Branch"
                            title="Save Branch"
                        />
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
