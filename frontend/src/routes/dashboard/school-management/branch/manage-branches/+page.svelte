<script lang="ts">
    import DataTable from "#lib/components/tables/DataTable.svelte";
    import type { PageProps } from "./$types";
    import type { BranchResponse } from "#lib/types/branches/branch.ts";

    const { data }: PageProps = $props();
</script>

<div>
    <DataTable {data} />
</div>
