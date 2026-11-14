<script lang="ts">
    import ClosePanelIcon from "@iconify-svelte/tabler/layout-navbar";
    import BuildingIcon from "@iconify-svelte/tabler/building";
    import BranchIcon from "@iconify-svelte/tabler/link";
    import { page } from "$app/state";

    const { children } = $props();
    interface Props {
        label: string;
        to: string;
        icon: any;
    }
    let SchoolManagementLinks: Props[] = [
        {
            label: "Profile",
            to: "/dashboard/school-management",
            icon: BuildingIcon,
        },

        {
            label: "Braches",
            to: "/dashboard/school-management/branches",
            icon: BranchIcon,
        },

        {
            label: "Departments",
            to: "/dashboard/school-management/departments",
            icon: "",
        },

        {
            label: "Users",
            to: "/dashboard/school-management/users",
            icon: "",
        },

        {
            label: "Roles & Permissions",
            to: "/dashboard/school-management/roles-permissions",
            icon: "",
        },

        {
            label: "School Settings",
            to: "/dashboard/school-management/school-settings",
            icon: "",
        },
    ];
</script>

<nav
    class="fixed h-screen overflow-hidden w-70 space-y-10 border-x bg-white border-gray-300 py-2 px-3"
>
    <div class="flex items-center justify-between">
        <div>
            <h1 class="first-letter:capitalize text-lg font-semibold">
                management
            </h1>
        </div>

        <div>
            <button
                aria-label="close panel button"
                title="Close Panel"
                class="flex items-center justify-center p-2 rounded-full bg-mauve-100 cursor-pointer"
            >
                <ClosePanelIcon height="1.3em" class="shrink-0" />
            </button>
        </div>
    </div>

    <div class="h-full overflow-auto scrollbar-thin">
        <div>
            <ul class="space-y-3">
                {#each SchoolManagementLinks as link (link.label)}
                    <li>
                        <a
                            href={link.to}
                            title={link.label}
                            class={[
                                "flex items-center gap-3 w-full hover:bg-purple-200 hover:text-purple-950 transition duration-300 py-3 px-4 rounded-full",
                                page.url.pathname === link.to
                                    ? "bg-purple-300 text-purple-950"
                                    : "",
                            ]}
                        >
                            <link.icon height="1.5em" class="shrink-0" />
                            <span class="">{link.label}</span>
                        </a>
                    </li>
                {/each}
            </ul>
        </div>
    </div>
</nav>

<main>
    <section class="ms-70">
        {@render children()}
    </section>
</main>
