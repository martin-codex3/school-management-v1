<script lang="ts">
    import type { SchoolResponse } from "#lib/types/school/school_response.ts";
    import { goto } from "$app/navigation";
    import { page } from "$app/state";
    import ChevronBackIcon from "@iconify-svelte/tabler/chevron-left";
    import type { PageProps } from "../$types";
    import BuildingIcon from "@iconify-svelte/tabler/buildings";
    import type { Component } from "svelte";
    import SchoolDetailsCard from "#lib/components/cards/SchoolDetailsCard.svelte";
    import { Icon } from "svelte-sonner";

    const { data }: PageProps = $props();

    interface Props {
        icon: any;
        title: string;
        description: string;
        value: string | undefined;
    }

    const schoolDetails: Props[] = $derived([
        {
            icon: BuildingIcon,
            title: "School name",
            description: "Current name",
            value: data.school.school_name,
        },

        {
            icon: BuildingIcon,
            title: "School type",
            description: "The school type",
            value: data.school.school_type,
        },

        {
            icon: BuildingIcon,
            title: "School email",
            description: "school email",
            value: data.school.school_email,
        },

        {
            icon: BuildingIcon,
            title: "School phone",
            description: "school contact",
            value: data.school.school_phone,
        },

        {
            icon: BuildingIcon,
            title: "address",
            description: "Schools address",
            value: data.school.address ?? "Not set",
        },

        {
            icon: BuildingIcon,
            title: "city",
            description: "school city",
            value: data.school.city ?? "Not set",
        },

        {
            icon: BuildingIcon,
            title: "country",
            description: "Current school location",
            value: data.school.country ?? "Not set",
        },
        {
            icon: BuildingIcon,
            title: "School name",
            description: "Name associated with the school",
            value: data.school.website_url ?? "Not set",
        },
    ]);

    let toggleUpdateModal: boolean = $state(false);
    // for opening and closing the modals here
    const handleOpenUpdateModal = () => {
        toggleUpdateModal = true;
    };

    const handleCloseUpdateModal = () => {
        toggleUpdateModal = false;
    };
</script>

<div class="h-screen flex items-center justify-center overflow-hidden">
    <div class="bg-white rounded-4xl px-10 py-5 h-[calc(100vh-1rem)] w-full">
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

            <h1 class="capitalize font-bold text-2xl">general information</h1>
        </div>

        <!-- for the information -->
        <div>
            {#each schoolDetails as school, index}
                <SchoolDetailsCard
                    Icon={school.icon}
                    value={school.value}
                    title={school.title}
                    description={school.description}
                    {index}
                    openModal={handleOpenUpdateModal}
                />
            {/each}
        </div>
    </div>
</div>
