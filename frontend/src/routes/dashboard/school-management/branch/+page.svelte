<script lang="ts">
    import TextInput from "#lib/components/inputs/TextInput.svelte";
    import { enhance } from "$app/forms";
</script>

<div class="h-screen overflow-hidden flex items-center justify-center">
    <div
        class="h-[calc(100vh-1rem)] bg-white w-full px-5 border border-gray-300 rounded-4xl"
    >
        <!-- for the main header -->
        <div class="h-full scrollbar-thin overflow-auto px-5 py-5">
            <div>
                <h1 class="text-2xl font-semibold capitalize">create branch</h1>
            </div>

            <!-- for the main form here -->
            <div>
                <form
                    action="?/createBranch"
                    method="POST"
                    use:enhance={() => {
                        return async () => {};
                    }}
                >
                    <div class="form__input__wrapper">
                        <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
                            <TextInput
                                type="text"
                                id="BranchName"
                                label="Branch name"
                                placeholder=""
                                value=""
                                valueError=""
                                name="branch_name"
                            />

                            <TextInput
                                type="email"
                                id="BranchEmail"
                                label="Branch email"
                                placeholder="branch@example.com"
                                value=""
                                valueError=""
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
                                valueError=""
                                name="branch_phone"
                            />

                            <TextInput
                                type="text"
                                id="AlternativePhone"
                                label="Alternative phone"
                                placeholder=""
                                value=""
                                valueError=""
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
                                valueError=""
                                name="address_line_1"
                            />

                            <TextInput
                                type="text"
                                id="AddressLine2"
                                label="Address line 2"
                                placeholder=""
                                value=""
                                valueError=""
                                name="address_line_2"
                            />
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
