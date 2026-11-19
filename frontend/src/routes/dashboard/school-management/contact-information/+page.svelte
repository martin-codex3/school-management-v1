<script lang="ts">
    import type { SchoolResponse } from "#lib/types/school/school_response.ts";
    import { goto } from "$app/navigation";
    import ChevronBackIcon from "@iconify-svelte/tabler/chevron-left";
    import BuildingIcon from "@iconify-svelte/tabler/buildings";
    import SchoolDetailsCard from "#lib/components/cards/SchoolDetailsCard.svelte";
    import BuildingsIcon from "@iconify-svelte/tabler/buildings";
    import MailIcon from "@iconify-svelte/tabler/mail";
    import PhoneIcon from "@iconify-svelte/tabler/phone";
    import MapPinIcon from "@iconify-svelte/tabler/map-pin";
    import MapIcon from "@iconify-svelte/tabler/map";
    import WorldIcon from "@iconify-svelte/tabler/world";
    import GlobeIcon from "@iconify-svelte/tabler/globe";
    import FileTextIcon from "@iconify-svelte/tabler/file-text";
    import HashIcon from "@iconify-svelte/tabler/hash";
    import InfoSquareIcon from "@iconify-svelte/tabler/info-square";
    import SettingsIcon from "@iconify-svelte/tabler/settings";
    import UpdateProfileModal from "#lib/components/modals/profile/UpdateProfileModal.svelte";
    import type { PageProps } from "./$types";
    import UpdateSchoolDetails from "#lib/components/modals/profile/schools/UpdateSchoolDetails.svelte";

    const { data, form }: PageProps = $props();

    interface Props {
        icon: any;
        title: string;
        description: string;
        value: string | undefined | object;
        name: string;
    }

    let fieldName: string = $state("");
    let fieldLabel: string = $state("");
    let fieldValue: string | boolean | undefined | object = $state("");

    const schoolDetails: Props[] = $derived([
        {
            icon: BuildingIcon,
            title: "School name",
            description: "Current name",
            value: data.school.school_name,
            name: "school_name",
        },
        {
            icon: BuildingsIcon,
            title: "School type",
            description: "The school type",
            value: data.school.school_type,
            name: "school_type",
        },
        {
            icon: MailIcon,
            title: "School email",
            description: "school email",
            value: data.school.school_email,
            name: "school_email",
        },
        {
            icon: PhoneIcon,
            title: "School phone",
            description: "school contact",
            value: data.school.school_phone,
            name: "school_phone",
        },
        {
            icon: MapPinIcon,
            title: "address",
            description: "Schools address",
            value: data.school.address ?? "Not set",
            name: "address",
        },
        {
            icon: MapIcon,
            title: "city",
            description: "school city",
            value: data.school.city ?? "Not set",
            name: "city",
        },
        {
            icon: WorldIcon,
            title: "country",
            description: "Current school location",
            value: data.school.country ?? "Not set",
            name: "country",
        },
        {
            icon: GlobeIcon,
            title: "School website",
            description: "Website url",
            value: data.school.website_url ?? "Not set",
            name: "website_url",
        },
        {
            icon: FileTextIcon,
            title: "Registration number",
            description: "Registration number",
            value: data.school.registration_number ?? "Not set",
            name: "registration_number",
        },
        {
            icon: HashIcon,
            title: "School code",
            description: "Name associated with the school",
            value: data.school.school_code ?? "Not set",
            name: "school_code",
        },
        {
            icon: InfoSquareIcon,
            title: "Description",
            description: "Description",
            value: data.school.description ?? "Not set",
            name: "description",
        },
        {
            icon: SettingsIcon,
            title: "School Settings",
            description: "All settings",
            value: data.school.settings ?? {},
            name: "school_settings",
        },
    ]);

    let toggleUpdateModal: boolean = $state(false);
    // for opening and closing the modals here
    const handleOpenUpdateModal = (
        name: string,
        value: string | boolean | undefined | object,
        label: string,
    ) => {
        toggleUpdateModal = true;

        if (toggleUpdateModal) {
            (fieldName = name), (fieldValue = value), (fieldLabel = label);
        }
    };

    const handleCloseUpdateModal = () => {
        toggleUpdateModal = false;
    };

    // for the truncanted schoolname
    const trucantedSchoolName = $derived(() => {
        return schoolDetails.find((s) =>
            s.name === "school_name"
                ? data.school.school_name.slice(0, 20)
                : s.value,
        );
    });

    const trucantedSchoolCode = $derived(() => {
        return `${data?.school.school_code?.slice(0, 20)}...`;
    });
</script>

<div class="h-screen flex items-center justify-center overflow-hidden">
    <div class="bg-white rounded-4xl px-5 py-5 h-[calc(100vh-1rem)] w-full">
        <div class="h-full overflow-auto scrollbar-thin px-5 space-y-10">
            <!-- for the upper header -->
            <div class="flex items-center gap-3">
                <button
                    aria-label="Go back button"
                    title="Go Back"
                    onclick={() => goto("/")}
                    class="flex items-center justify-center p-3 rounded-full bg-gray-100 cursor-pointer hover:drop-shadow-sm transition duration-200"
                >
                    <ChevronBackIcon height="1.3em" />
                </button>

                <h1 class="capitalize font-bold text-2xl">
                    general information
                </h1>
            </div>

            <!-- for the information -->
            <div class="space-y-1">
                {#each schoolDetails as school, index}
                    <SchoolDetailsCard
                        Icon={school.icon}
                        value={school.name === "school_name"
                            ? data.school.school_name.slice(0, 20)
                            : school.value && school.name === "school_code"
                              ? data.school.school_code?.slice(0, 20)
                              : school.value && school.name === "description"
                                ? data.school.description?.slice(0, 20)
                                : school.value}
                        title={school.title}
                        description={school.description}
                        {index}
                        length={schoolDetails.length}
                        name={school.name}
                        openModal={() =>
                            handleOpenUpdateModal(
                                school.name,
                                school.value,
                                school.title,
                            )}
                    />
                {/each}
            </div>
        </div>
    </div>
</div>

<!-- for the modals here -->
{#if toggleUpdateModal}
    <UpdateSchoolDetails
        closeModal={handleCloseUpdateModal}
        toggleModal={toggleUpdateModal}
        name={fieldName}
        label={fieldLabel}
        {fieldValue}
        {form}
    />
{/if}
