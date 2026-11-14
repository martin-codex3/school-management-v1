<script lang="ts">
    import type { LayoutProps } from "./$types";
    import BuildingIcon from "@iconify-svelte/tabler/buildings";
    import CalendarWeek from "@iconify-svelte/tabler/calendar-week";
    import UsersIcon from "@iconify-svelte/tabler/users";
    import CalendarChekIcon from "@iconify-svelte/tabler/calendar-check";
    import FinancesIcon from "@iconify-svelte/tabler/moneybag";
    import MessagesIcon from "@iconify-svelte/tabler/message";
    import SchoolOperationsIcon from "@iconify-svelte/tabler/stack-3";
    import ChartIcon from "@iconify-svelte/tabler/chart-infographic";
    import ChevronIcon from "@iconify-svelte/tabler/chevron-right";
    import DashboardIcon from "@iconify-svelte/tabler/dashboard";
    import { page } from "$app/state";

    let { children, data }: LayoutProps = $props();

    interface Props {
        label: string;
        to: string;
        icon: any;
    }

    // for the school management links
    const schoolManagementLinks: Props[] = [
        {
            label: "Dashboard",
            to: "/dashboard",
            icon: DashboardIcon,
        },

        {
            label: "School Management",
            to: "/dashboard/school-management",
            icon: BuildingIcon,
        },

        {
            label: "Academic Management",
            to: "/dashboard/school-management/academic-management",
            icon: CalendarWeek,
        },

        {
            label: "People Management",
            to: "/dashboard/school-management/people-management",
            icon: UsersIcon,
        },

        {
            label: "Academics",
            to: "/dashboard/school-management/academics",
            icon: CalendarChekIcon,
        },

        {
            label: "Finances",
            to: "/dashboard/school-management/finances",
            icon: FinancesIcon,
        },

        {
            label: "Communications",
            to: "/dashboard/school-management/communications",
            icon: MessagesIcon,
        },

        {
            label: "School Operations",
            to: "/dashboard/school-management/school-operations",
            icon: SchoolOperationsIcon,
        },

        {
            label: "Reports and Settings",
            to: "/dashboard/school-management/reports-and-settings",
            icon: ChartIcon,
        },
    ];
</script>

<nav
    class="bg-white h-screen w-80 fixed top-0 overflow-hidden flex flex-col items-stretch py-3 px-5 justify-between space-y-5"
>
    <!-- for the app logo -->
    <div>
        <h1>main logo</h1>
    </div>

    <!-- for the main links -->
    <div class="h-full overflow-auto scrollbar-thin">
        <div class="space-y-2">
            <!-- for school management links -->
            <div>
                <h1 class="capitalize text-sm text-gray-400 font-semibold">
                    school management
                </h1>
            </div>
            <div>
                <ul class="w-full space-y-2">
                    {#each schoolManagementLinks as link}
                        <li class="w-full">
                            <a
                                href={link.to}
                                title={link.label}
                                class={[
                                    "flex items-center w-full gap-3 hover:bg-purple-200 hover:text-purple-950 rounded-full px-2 py-2 transition duration-300",
                                    page.url.pathname === link.to
                                        ? "bg-purple-300"
                                        : "",
                                ]}
                            >
                                <link.icon height="1.7em" class="shrink-0" />
                                <span class="text-lg">{link.label}</span>
                            </a>
                        </li>
                    {/each}
                </ul>
            </div>
        </div>
    </div>

    <!-- for the profile links here -->
    <div>
        <div
            class="rounded-tr-4xl rounded-tl-4xl rounded-bl-xl rounded-br-xl bg-purple-300 px-3 py-3"
        >
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-3">
                    <div
                        class="h-14 w-14 rounded-full bg-black/60 flex items-center justify-center"
                    >
                        <h1 class="font-bold uppercase text-white">MS</h1>
                    </div>

                    <div>
                        <h1 class="text-lg font-semibold">
                            {data.user.first_name}
                        </h1>

                        <p>Online</p>
                    </div>
                </div>

                <div>
                    <a
                        href="/dashboard/profile"
                        title="Check your profile"
                        class="flex items-center justify-center p-2 rounded-full bg-purple-400 text-purple-700"
                    >
                        <ChevronIcon height="1.3em" class="shrink-0" />
                    </a>
                </div>
            </div>
        </div>
    </div>
</nav>

<main>
    <section class="ms-80">
        {@render children()}
    </section>
</main>
