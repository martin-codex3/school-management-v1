<script lang="ts">
    const {
        id,
        placeholder,
        name,
        label,
        children,
        fieldError,
    }: {
        id: string;
        placeholder: string;
        name: string;
        label: string;
        fieldError: string | undefined;
        children: any;
    } = $props();
</script>

{#snippet Options()}
    <option></option>
{/snippet}

{#snippet fieldErrors(errorValue: string | undefined)}
    <span class="text-sm text-red-600">{errorValue}</span>
{/snippet}

<div class="">
    {#if label}
        <label for={id}>{label}</label>
    {/if}
    <select
        {name}
        {id}
        {placeholder}
        class={[
            "w-full mt-1 py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-purple focus:ring-primary-main-purple",
            fieldError ? "bg-red-50 border-red-600" : "",
        ]}
    >
        {@render children()}
    </select>
    {@render fieldErrors(fieldError)}
</div>
