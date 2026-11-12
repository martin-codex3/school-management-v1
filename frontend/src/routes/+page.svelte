<script lang="ts">
    import SelectInput from "#lib/components/inputs/SelectInput.svelte";
    import SelectInpu from "#lib/components/inputs/SelectInput.svelte";
    import TextInput from "#lib/components/inputs/TextInput.svelte";
</script>

<section class="h-screen flex items-center justify-center">
    <div
        class="bg-white rounded-4xl w-full border border-primary-border max-w-2xl h-[calc(100vh-3rem)] mx-auto"
    >
        <div class="h-full overflow-auto scrollbar-thin px-10 py-5">
            <div class="flex items-center justify-center">
                <button
                    aria-label="options button"
                    title="Sign In"
                    class="flex items-center justify-center p-3 rounded-full border"
                ></button>
            </div>

            <div>
                <form action="">
                    <div class="wrapper">
                        <div
                            class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-5"
                        >
                            <TextInput
                                type="text"
                                name="first_name"
                                placeholder="John"
                                id="FirstName"
                                label="First name"
                            />

                            <TextInput
                                type="text"
                                name="last_name"
                                placeholder="Doe"
                                id="LastName"
                                label="Last name"
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
                            />

                            <TextInput
                                type="text"
                                name="phone_number"
                                placeholder=""
                                id="PhoneNumber"
                                label="Phone number"
                            />
                        </div>

                        <div
                            class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-5"
                        >
                            <TextInput
                                type="text"
                                name="first_name"
                                placeholder="John"
                                id="FirstName"
                                label="First name"
                            />

                            <TextInput
                                type="text"
                                name="last_name"
                                placeholder="Doe"
                                id="LastName"
                                label="Last name"
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
                            />

                            <SelectInput
                                name="school_type"
                                id="SchoolType"
                                placeholder=""
                                label="School type"
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
                            />

                            <TextInput
                                type="text"
                                name="school_phone"
                                placeholder=""
                                id="SchoolPhone"
                                label="School phone"
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
                            />

                            <TextInput
                                type="text"
                                name="city"
                                placeholder="Blantyre"
                                id="City"
                                label="City"
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
                            >
                                <option value="">Selection option</option>
                                <option value="Malawi">Malawi</option>
                            </SelectInput>
                        </div>

                        <div
                            class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-5"
                        >
                            <TextInput
                                type="password"
                                name="password_hash"
                                placeholder=""
                                id="Password"
                                label="Password"
                            />

                            <TextInput
                                type="text"
                                name="confirm_password"
                                placeholder=""
                                id="ConfirmPassword"
                                label="Confirm password"
                            />
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</section>
