<script lang="ts">
    import ProfileCard from "#lib/components/cards/ProfileCard.svelte";
    import type { PageProps } from "../$types";
    import ProfileIcon from "@iconify-svelte/tabler/user";
    import Emailcon from "@iconify-svelte/tabler/mail";
    import PhoneNumberIcon from "@iconify-svelte/tabler/phone";
    import BiographyIcon from "@iconify-svelte/tabler/file-text";
    import ProfileeImageIcon from "@iconify-svelte/tabler/photo";

    interface Props {
        label: string;
        title: string;
        description: string;
        iconData: any;
        value: any;
    }
    let { data }: PageProps = $props();

    let profileData: Props[] = $derived([
        {
            label: "First name",
            title: "Open Update Modal",
            description: "The first name associated with your account",
            iconData: ProfileIcon,
            value: data.user.first_name,
        },

        {
            label: "Last name",
            title: "Open Update Modal",
            description: "The last name associated with your account",
            iconData: ProfileIcon,
            value: data.user.last_name,
        },

        {
            label: "Email",
            title: "Open Update Modal",
            description: "your account email",
            iconData: Emailcon,
            value: data.user.email,
        },

        {
            label: "Phone number",
            title: "Open Update Modal",
            description: "Your contact phone number",
            iconData: PhoneNumberIcon,
            value: data.user.phone_number,
        },

        {
            label: "Bio",
            title: "Open Update Modal",
            description: "Account biography",
            iconData: BiographyIcon,
            value: data.user.bio ?? "Not set",
        },

        {
            label: "Profile Image",
            title: "Open Update Modal",
            description: "Your profile image path",
            iconData: ProfileeImageIcon,
            value: data.user.profile_image_url ?? "Not set",
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
                        description={profile.description}
                        title={profile.title}
                        label={profile.label}
                    />
                {/each}
            </div>
        </div>
    </div>
</div>
