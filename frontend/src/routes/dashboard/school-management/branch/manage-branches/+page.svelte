<script lang="ts">
    import type { BranchData } from "#lib/types/branches/branch_data.ts";
    import {
        createSortedRowModel,
        createTable,
        FlexRender,
        rowSortingFeature,
        sortFn_alphanumeric,
        sortFn_datetime,
        sortFn_text,
        tableFeatures,
        type ColumnDef,
    } from "@tanstack/svelte-table";

    import IconArrowsUpDown from "@iconify-svelte/tabler/arrows-up-down";

    import type { PageProps } from "./$types";

    const { data }: PageProps = $props();

    // tables features
    const features = tableFeatures({
        rowSortingFeature,
        sortedRowModel: createSortedRowModel(),
        sortFns: {
            alphaNumeric: sortFn_alphanumeric,
            text: sortFn_text,
            datetime: sortFn_datetime,
        },
    });

    // table columns
    const columns: ColumnDef<typeof features, BranchData>[] = [
        {
            accessorKey: "branch_name",
            header: "Name",
            sortFn: "auto",
        },

        {
            accessorKey: "branch_phone",
            header: "Phone",
            sortFn: "auto",
        },

        {
            accessorKey: "created_date",
            header: "Created date",
            sortFn: "datetime",
        },
    ];

    // the table instance
    const table = createTable({
        features,
        columns,
        enableSorting: true,
        enableMultiSort: true,
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
                                <th
                                    onclick={header.column.getToggleSortingHandler()}
                                    class="p-4 text-start font-normal"
                                >
                                    {#if !header.isPlaceholder}
                                        <div class="flex items-center gap-2">
                                            <FlexRender {header} />

                                            {#if header.column.getIsSorted() === "asc"}
                                                <h1>1</h1>
                                            {:else if header.column.getIsSorted() === "desc"}
                                                <h1>2</h1>
                                            {:else if header.column.getCanSort()}
                                                <IconArrowsUpDown
                                                    height="1em"
                                                />
                                            {/if}
                                        </div>
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
