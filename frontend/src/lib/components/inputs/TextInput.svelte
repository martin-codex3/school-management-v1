<script lang="ts">
    interface Props {
        type: string;
        id: string;
        placeholder: string;
        name: string;
        label: string;
    }

    const { type, id, placeholder, name, label }: Props = $props();
</script>

<div class="">
    {#if label}
        <label for={id}>{label}</label>
    {/if}
    <input
        {type}
        {id}
        {placeholder}
        {name}
        class="w-full mt-1 py-3 px-3 rounded-lg outline-none border border-gray-300 focus:border-primary-main-green focus:ring-primary-main-green"
    />
</div>
