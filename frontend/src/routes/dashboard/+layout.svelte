<script lang="ts">
    import type { LayoutProps } from "./$types";

    let { children, data }: LayoutProps = $props();

    interface Props {
        label: string;
        to: string;
        icon: string;
    }

    // for the school management links
    const schoolManagementLinks: Props[] = [
        {
            label: "School Profile",
            to: "/dashboard/school-management/school-profile",
            icon: "",
        },

        {
            label: "Branches",
            to: "/dashboard/school-management/academic-management",
            icon: "",
        },

        {
            label: "Departments",
            to: "/dashboard/school-management/people-management",
            icon: "",
        },

        {
            label: "Academics",
            to: "/dashboard/school-management/academics",
            icon: "",
        },

        {
            label: "Finances",
            to: "/dashboard/school-management/finances",
            icon: "",
        },

        {
            label: "Communications",
            to: "/dashboard/school-management/communications",
            icon: "",
        },

        {
            label: "School Operations",
            to: "/dashboard/school-management/school-operations",
            icon: "",
        },

        {
            label: "Reports and Settings",
            to: "/dashboard/school-management/reports-and-settings",
            icon: "",
        },
    ];
</script>

<main>
    <nav
        class="bg-white h-screen w-80 fixed top-0 overflow-hidden flex flex-col items-start py-5 px-5 justify-between space-y-5"
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
                    <ul class="">
                        {#each schoolManagementLinks as link}
                            <li class="">
                                <a
                                    href={link.to}
                                    title={link.label}
                                    class="block bg-purple-400 w-full"
                                >
                                    <span>{link.label}</span>
                                </a>
                            </li>
                        {/each}
                    </ul>
                </div>
            </div>
        </div>

        <!-- for the profile links here -->
        <div>
            <h1>{data.user.email}</h1>
        </div>
    </nav>

    <section class="ms-80">
        {@render children()}
    </section>
</main>
