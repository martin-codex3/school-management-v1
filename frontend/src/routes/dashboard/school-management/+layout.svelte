<script lang="ts">
    import ClosePanelIcon from "@iconify-svelte/tabler/layout-navbar";
    import BuildingIcon from "@iconify-svelte/tabler/building";
    import SitemapIcon from "@iconify-svelte/tabler/sitemap";
    import HierarchyIcon from "@iconify-svelte/tabler/hierarchy";
    import UsersIcon from "@iconify-svelte/tabler/users";
    import ShieldCheckIcon from "@iconify-svelte/tabler/shield-check";
    import SettingsIcon from "@iconify-svelte/tabler/settings";
    import { page } from "$app/state";

    const { children } = $props();

    interface Props {
        label: string;
        to: string;
        icon: any;
    }

    let SchoolManagementLinks: Props[] = [
        {
            label: "School Profile",
            to: "/dashboard/school-management",
            icon: BuildingIcon,
        },
        {
            label: "Branches",
            to: "/dashboard/school-management/branch",
            icon: SitemapIcon,
        },
        {
            label: "Departments",
            to: "/dashboard/school-management/departments",
            icon: HierarchyIcon,
        },
        {
            label: "Users",
            to: "/dashboard/school-management/users",
            icon: UsersIcon,
        },
        {
            label: "Roles & Permissions",
            to: "/dashboard/school-management/roles-permissions",
            icon: ShieldCheckIcon,
        },
        {
            label: "School Settings",
            to: "/dashboard/school-management/school-settings",
            icon: SettingsIcon,
        },
    ];
</script>

<nav
    class="fixed h-screen overflow-hidden w-90 space-y-10 border-x bg-white border-gray-300 py-2 px-3"
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
    <section class="ms-90 px-5">
        {@render children()}
    </section>
</main>
