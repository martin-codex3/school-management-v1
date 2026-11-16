<script lang="ts">
    import type { Component } from "svelte";
    import EditIcon from "@iconify-svelte/tabler/pencil";

    interface Props {
        Icon: Component;
        value: string | undefined | object;
        title: string;
        description: string;
        index: number;
        openModal: () => void;
    }

    const { Icon, value, title, description, index, openModal }: Props =
        $props();

    const currentIndex = $derived(index + 1);
</script>

<!-- we will hae the card header -->
{#snippet cardHeader(title: string, description: string, Icon: Component)}
    <div class="flex items-center gap-5">
        <div>
            <Icon height="1.5em"></Icon>
        </div>

        <div>
            <h1 class="text-lg capitalize font-semibold">{title}</h1>
            <p class="text-lg first-letter:uppercase">{description}</p>
        </div>
    </div>
{/snippet}

<!-- we will also have the card body -->

{#snippet cardBody(value: string | undefined | object)}
    <div class="flex items-center gap-5">
        <div>
            <h2>{value}</h2>
        </div>

        <div>
            <button
                aria-label="for opening the modal"
                {title}
                onclick={openModal}
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
    {@render cardHeader(title, description, Icon)}
    {@render cardBody(value)}
</div>
