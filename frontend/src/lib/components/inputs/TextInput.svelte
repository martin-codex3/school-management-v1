<script lang="ts">
    interface Props {
        type: string;
        id: string;
        placeholder: string;
        name: string;
        label: string;
        valueError: string | undefined;
    }

    const {
        type,
        id,
        placeholder,
        name,
        label,
        valueError = "",
    }: Props = $props();
</script>

{#snippet fieldError(error: string | undefined)}
    <span class="text-sm text-red-600">{error}</span>
{/snippet}

<div class="">
    {#if label}
        <label for={id}>{label}</label>
    {/if}
    <input
        {type}
        {id}
        {placeholder}
        {name}
        class={[
            "w-full mt-1 py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-purple focus:ring-primary-main-purple",
            valueError ? "bg-red-50 border-red-600" : "",
        ]}
    />
    {@render fieldError(valueError)}
</div>
