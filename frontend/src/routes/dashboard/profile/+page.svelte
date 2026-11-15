<script lang="ts">
    import ProfileCard from "#lib/components/cards/ProfileCard.svelte";
    import type { UserResponse } from "#lib/types/users/user_response.ts";
    import type { PageProps } from "../$types";
    import ProfileIcon from "@iconify-svelte/tabler/user";

    interface Props {
        label: string;
        title: string;
        description: string;
        iconData: any;
        value: any;
    }
    let { data }: PageProps = $props();

    let profileData: Props[] = $state([
        {
            label: "First name",
            title: "Open Update Modal",
            description: "The name associated with your accoun",
            iconData: ProfileIcon,
            value: "",
        },

        {
            label: "Last name",
            title: "Open Update Modal",
            description: "The name associated with your accoun",
            iconData: "",
            value: "",
        },

        {
            label: "Email",
            title: "Open Update Modal",
            description: "The name associated with your accoun",
            iconData: "",
            value: "",
        },

        {
            label: "Phone number",
            title: "Open Update Modal",
            description: "The name associated with your accoun",
            iconData: "",
            onclick: () => {},
            value: "",
        },

        {
            label: "Bio",
            title: "Open Update Modal",
            description: "The name associated with your accoun",
            iconData: "",
            value: "",
        },

        {
            label: "Profile Image",
            title: "Open Update Modal",
            description: "The name associated with your accoun",
            iconData: "",
            value: "",
        },
    ]);
</script>

<div class="">
    <div class="h-screen flex items-center justify-center">
        <div
            class="bg-white rounded-4xl w-full max-w-3xl h-[calc(100vh-2rem)] space-y-10 mx-auto px-10 py-5"
        >
            <!-- for the main header -->
            <div
                class="flex items-center gap-3 w-full border border-gray-300 bg-gray-50 rounded-full px-2 py-2"
            >
                <div class="h-20 w-20 rounded-full bg-purple-400"></div>
                <div>
                    <h1 class="text-lg capitalize font-semibold">
                        {data.user.first_name}
                    </h1>
                    <p>{data.user.email}</p>
                </div>
            </div>

            <!-- for the main content here -->
            <div class="">
                {#each profileData as profile}
                    <ProfileCard
                        value={profile.value}
                        Icon={profile.iconData}
                    />
                {/each}
            </div>
        </div>
    </div>
</div>
