<script lang="ts">
    import type { BranchData } from "#lib/types/branches/branch_data.ts";
    import {
        createTable,
        FlexRender,
        tableFeatures,
        type ColumnDef,
    } from "@tanstack/svelte-table";

    import type { PageProps } from "./$types";

    const { data }: PageProps = $props();

    // tables features
    const features = tableFeatures({});

    // table columns
    const columns: ColumnDef<typeof features, BranchData>[] = [
        {
            accessorKey: "branch_name",
            header: "Branch name",
        },

        {
            accessorKey: "branch_email",
            header: "Branch email",
        },

        {
            accessorKey: "branch_phone",
            header: "Branch phone",
        },

        {
            accessorKey: "created_date",
            header: "Created date",
        },
    ];

    // the table instance
    const table = createTable({
        features,
        columns,
        get data() {
            return data.branches;
        },
    });
</script>

<div class="h-screen flex items-center justify-center">
    <div
        class="h-[calc(100vh-1rem)] overflow-hidden flex flex-col justify-between px-5 bg-primary-white rounded-4xl w-full"
    >
        <!-- for the table header -->
        <div class="">
            <h1 class="text-xl font-semibold capitalize">manage branches</h1>
        </div>

        <!-- for the main table controllers -->
        <div class="h-full overflow-auto scrollbar-none py-4">
            <!-- for the table body -->
            <table class="w-full table-auto border-collapse">
                <thead>
                    {#each table.getHeaderGroups() as headerGroup (headerGroup.id)}
                        <tr>
                            {#each headerGroup.headers as header (header.id)}
                                <th class="p-4 text-start font-semibold">
                                    {#if !header.isPlaceholder}
                                        <FlexRender {header} />
                                    {/if}
                                </th>
                            {/each}
                        </tr>
                    {/each}
                </thead>

                <tbody>
                    {#each table.getRowModel().rows as rows (rows.id)}
                        <tr>
                            {#each rows.getAllCells() as cell (cell.id)}
                                <td>
                                    <FlexRender {cell} />
                                </td>
                            {/each}
                        </tr>
                    {/each}
                </tbody>
            </table>
        </div>

        <!-- for the table footer -->
        <div class="">
            <h1>table footer</h1>
        </div>
    </div>
</div>
