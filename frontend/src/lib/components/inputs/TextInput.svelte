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

<div>
    {#if label}
        <label for={id}>{label}</label>
    {/if}
    <input {type} {id} {placeholder} {name} />
</div>
