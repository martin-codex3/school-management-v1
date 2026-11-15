<script lang="ts">
    import type { Component } from "svelte";
    import EditIcon from "@iconify-svelte/tabler/pencil";

    interface Props {
        Icon: Component;
        value: string;
        title: string;
        description: string;
        label: string;
    }

    const { Icon, value, title, description, label }: Props = $props();
</script>

<!-- we will hae the card header -->
{#snippet cardHeader(label: string, description: string, Icon: Component)}
    <div class="flex items-center gap-5">
        <div>
            <Icon height="1.5em"></Icon>
        </div>

        <div>
            <h1>{label}</h1>
            <p>{description}</p>
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
                class="flex items-center justify-center p-2 rounded-full hover:bg-gray-100"
            >
                <EditIcon height="2em" />
            </button>
        </div>
    </div>
{/snippet}
<div class={["flex items-center justify-between bg-gray-100"]}>
    <!-- card header -->
    {@render cardHeader(label, description, Icon)}
    {@render profileBody(title, value)}
</div>
