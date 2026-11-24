<script lang="ts">
    import type { PageProps } from "./$types";

    const { data }: PageProps = $props();

    $inspect(data.branches);
</script>

<div>
    <h1>{data.branches}</h1>
</div>
