<script lang="ts">
    const {
        id,
        placeholder,
        name,
        label,
        children,
    }: {
        id: string;
        placeholder: string;
        name: string;
        label: string;
        children: any;
    } = $props();
</script>

{#snippet Options()}
    <option></option>
{/snippet}

<div class="">
    {#if label}
        <label for={id}>{label}</label>
    {/if}
    <select
        {name}
        {id}
        {placeholder}
        class="w-full mt-1 py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-purple focus:ring-primary-main-purple"
    >
        {@render children()}
    </select>
</div>
