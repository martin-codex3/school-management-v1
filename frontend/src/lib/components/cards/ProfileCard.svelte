<script lang="ts">
    import type { Component } from "svelte";

    interface Props {
        Icon: Component;
        value: string;
        title: string;
        description: string;
    }

    const { Icon, value }: Props = $props();
</script>

<!-- we will hae the card header -->
{#snippet cardHeader(value: string, Icon: Component)}
    <div class="flex items-center gap-5">
        <div>
            <Icon height="1.5em"></Icon>
        </div>

        <div>
            <h1>name</h1>
            <p>value</p>
        </div>
    </div>
{/snippet}

<!-- we will also have the card body -->
<div>
    <!-- card header -->
    {@render cardHeader(value, Icon)}
</div>
