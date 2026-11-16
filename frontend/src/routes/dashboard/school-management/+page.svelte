<script lang="ts">
    import type { PageProps } from "./$types";
    import BuildingIcon from "@iconify-svelte/tabler/buildings";
    import ContactIcon from "@iconify-svelte/tabler/phone";
    import LocationIcon from "@iconify-svelte/tabler/location";
    import SchoolDetailsIcon from "@iconify-svelte/tabler/school";
    import LeaderShipIcon from "@iconify-svelte/tabler/users";
    import BrandingIcon from "@iconify-svelte/tabler/color-picker";
    import DocumentIcon from "@iconify-svelte/tabler/files";
    let { data }: PageProps = $props();

    interface Props {
        to: string;
        title: string;
        icon: any;
        description: string;
    }

    const dashboardLinks: Props[] = $state([
        {
            to: "/dashboard/school-profile/general-information",
            title: "General identity and registration",
            description: "School identity and registration",
            icon: BuildingIcon,
        },

        {
            to: "/dashboard/school-profile/contact-information",
            title: "Contact information",
            description: "Email and telephone details",
            icon: ContactIcon,
        },

        {
            to: "/dashboard/school-profile/address",
            title: "Address & location",
            description: "Registered school address",
            icon: LocationIcon,
        },

        {
            to: "/dashboard/school-profile/school-details",
            title: "School details",
            description: "School identity and registration",
            icon: SchoolDetailsIcon,
        },

        {
            to: "/dashboard/school-profile/leadership",
            title: "Principal & management",
            description: "Principal and management",
            icon: LeaderShipIcon,
        },

        {
            to: "/dashboard/school-profile/branding",
            title: "Branding",
            description: "Logos and colours",
            icon: BrandingIcon,
        },

        {
            to: "/dashboard/school-profile/documents",
            title: "Documents",
            description: "Registration and accreditation records",
            icon: DocumentIcon,
        },
    ]);
</script>

<div class="h-screen flex items-center justify-center px-5 overflow-hidden">
    <div
        class="h-[calc(100vh-1rem)] bg-white rounded-4xl border py-5 px-5 border-gray-300 w-full"
    >
        <div class="h-full overflow-auto scrollbar-thin px-5 space-y-10">
            <!-- for the card header -->
            <div class="flex items-start justify-between">
                <div class="flex items-start gap-3">
                    <div class="h-32 w-32 bg-purple-200 rounded-xl"></div>
                    <div>
                        <h1 class="text-2xl font-bold capitalize">
                            {data.school.school_name}
                        </h1>
                        <h1 class="text-lg first-letter:uppercase">
                            {data.school.school_email}
                        </h1>
                        <p class="text-gray-400">{data.school.school_type}</p>
                    </div>
                </div>

                <div>
                    <div
                        class="bg-green-200 text-green-800 px-5 py-px rounded-full"
                    >
                        <h3 class="font-semibold">active</h3>
                    </div>
                </div>
            </div>

            <!-- for the links here  -->
            <div class="">
                <div
                    class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 gap-5"
                >
                    {#each dashboardLinks as link (link.title)}
                        <div
                            class="border border-gray-400 bg-gray-100 px-5 py-3 space-y-5 rounded-xl"
                        >
                            <link.icon height="2em" class="shrink-0" />
                            <div class="space-y-2">
                                <h1 class="text-xl font-bold capitalize">
                                    {link.title}
                                </h1>
                                <p class="text-lg">
                                    {link.description}
                                </p>
                            </div>
                        </div>
                    {/each}
                </div>
            </div>
        </div>
    </div>
</div>
