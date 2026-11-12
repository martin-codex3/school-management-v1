<script lang="ts">
    import LoadingSVG from "@iconify-svelte/svg-spinners/180-ring";
    interface Props {
        isLoading: boolean;
        title: string;
        label: string;
    }

    const { isLoading, title, label }: Props = $props();
</script>

<div>
    <button
        aria-label="Custom styled button"
        {title}
        class="flex items-center justify-center w-44 h-10 rounded-full bg-primary-main-purple capitalize"
    >
        {#if isLoading}
            <LoadingSVG height="1.3em" />
        {:else}
            <span>{label}</span>
        {/if}
    </button>
</div>
