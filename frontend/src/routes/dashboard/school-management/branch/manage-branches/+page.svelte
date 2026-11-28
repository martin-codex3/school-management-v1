<script lang="ts">
    import type { BranchData } from "#lib/types/branches/branch_data.ts";
    import {
        createTable,
        FlexRender,
        rowSortingFeature,
        tableFeatures,
        type ColumnDef,
    } from "@tanstack/svelte-table";

    import IconArrowsUpDown from "@iconify-svelte/tabler/arrows-up-down";

    import type { PageProps } from "./$types";

    const { data }: PageProps = $props();

    // tables features
    const features = tableFeatures({ rowSortingFeature });

    // table columns
    const columns: ColumnDef<typeof features, BranchData>[] = [
        {
            accessorKey: "branch_name",
            header: "Branch name",
        },

        {
            accessorKey: "branch_phone",
            header: "Branch phone",
        },

        {
            accessorKey: "created_date",
            header: "Created date",
        },

        {
            accessorKey: "updated_date",
            header: "Updated date",
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
        class="h-[calc(100vh-1rem)] overflow-hidden flex flex-col justify-between bg-primary-white rounded-4xl w-full"
    >
        <!-- for the table header -->
        <div class="p-5">
            <h1 class="text-xl font-semibold capitalize">manage branches</h1>
        </div>

        <!-- for the main table controllers -->
        <div class="h-full overflow-auto scrollbar-none py-4">
            <!-- for the table body -->
            <table class="w-full table-auto border-collapse">
                <thead>
                    {#each table.getHeaderGroups() as headerGroup (headerGroup.id)}
                        <tr class="border-b border-b-gray-300 bg-purple-50">
                            {#each headerGroup.headers as header (header.id)}
                                <th class="p-4 text-start font-normal">
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
                        <tr
                            class="border-b border-b-gray-300 odd:bg-gray-100 even:bg-white"
                        >
                            {#each rows.getAllCells() as cell (cell.id)}
                                <td class="p-4 py-4 text-start">
                                    <FlexRender {cell} />
                                </td>
                            {/each}
                        </tr>
                    {/each}
                </tbody>
            </table>
        </div>

        <!-- for the table footer -->
        <div class="p-5">
            <h1>table footer</h1>
        </div>
    </div>
</div>
