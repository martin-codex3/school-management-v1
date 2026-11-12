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
        class="flex items-center justify-center w-44 h-12 text-purple-200 font-semibold rounded-full bg-primary-main-purple capitalize"
    >
        {#if isLoading}
            <div class="flex items-center gap-2">
                <LoadingSVG height="1.3em" class="shrink-0" />
                <p class="text-sm">Processing...</p>
            </div>
        {:else}
            <span>{label}</span>
        {/if}
    </button>
</div>
