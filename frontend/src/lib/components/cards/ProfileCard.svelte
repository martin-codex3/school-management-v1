<script lang="ts">
    import type { Component } from "svelte";
    import EditIcon from "@iconify-svelte/tabler/pencil";

    interface Props {
        Icon: Component;
        value: string;
        title: string;
        description: string;
        label: string;
        index: number;
    }

    const { Icon, value, title, description, label, index }: Props = $props();

    const currentIndex = $derived(index + 1);
</script>

<!-- we will hae the card header -->
{#snippet cardHeader(label: string, description: string, Icon: Component)}
    <div class="flex items-center gap-5">
        <div>
            <Icon height="1.5em"></Icon>
        </div>

        <div>
            <h1 class="text-lg capitalize font-semibold">{label}</h1>
            <p class="text-lg first-letter:uppercase">{description}</p>
        </div>
    </div>
{/snippet}

<!-- we will also have the card body -->

{#snippet profileBody(title: string, value: string)}
    <div class="flex items-center gap-5">
        <div>
            <h2>{value}</h2>
        </div>

        <div>
            <button
                aria-label="for opening the modal"
                {title}
                class="flex items-center justify-center p-2 rounded-full hover:bg-purple-200 hover:text-purple-950 cursor-pointer transition duration-300"
            >
                <EditIcon height="1.5em" />
            </button>
        </div>
    </div>
{/snippet}
<div
    class={[
        "flex items-center justify-between bg-gray-100 px-3 py-2",
        currentIndex === 1
            ? "rounded-tr-3xl rounded-tl-3xl rounded-bl-lg rounded-br-lg"
            : "rounded-lg",

        currentIndex === 6 ? "rounded-bl-3xl rounded-br-3xl" : "",
    ]}
>
    <!-- card header -->
    {@render cardHeader(label, description, Icon)}
    {@render profileBody(title, value)}
</div>
