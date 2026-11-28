<script lang="ts">
    import type { BranchData } from "#lib/types/branches/branch_data.ts";
    import {
        columnFilteringFeature,
        createFilteredRowModel,
        createSortedRowModel,
        createTable,
        filterFn_includesString,
        FlexRender,
        rowSortingFeature,
        sortFn_alphanumeric,
        sortFn_datetime,
        sortFn_text,
        tableFeatures,
        type ColumnDef,
    } from "@tanstack/svelte-table";

    import IconArrowsUpDown from "@iconify-svelte/tabler/arrows-up-down";
    import IconSortAscending from "@iconify-svelte/tabler/sort-ascending";
    import IconSortDescensing from "@iconify-svelte/tabler/sort-descending";
    import IconDotsVertical from "@iconify-svelte/tabler/dots-vertical";
    import IconFilter from "@iconify-svelte/tabler/filter";

    import type { PageProps } from "./$types";

    const { data }: PageProps = $props();

    // tables features
    const features = tableFeatures({
        rowSortingFeature,
        columnFilteringFeature,
        filteredRowModel: createFilteredRowModel(),
        sortedRowModel: createSortedRowModel(),
        sortFns: {
            alphaNumeric: sortFn_alphanumeric,
            text: sortFn_text,
            datetime: sortFn_datetime,
        },
        filterFns: {
            includesString: filterFn_includesString,
        },
    });

    // table columns
    const columns: ColumnDef<typeof features, BranchData>[] = [
        {
            accessorKey: "branch_name",
            header: "Name",
            sortFn: "auto",
            filterFn: "includesString",
        },

        {
            accessorKey: "branch_phone",
            header: "Phone",
            sortFn: "auto",
            filterFn: "includesString",
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
        enableColumnFilters: true,
        enableFilters: true,
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
        <div class="p-5 flex items-center justify-between">
            <div>
                <input type="search" class="w-full flex-1" />
            </div>

            <div class="flex items-center">
                <button>
                    <span>
                        <h1>hie</h1>
                    </span>
                </button>
            </div>
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
                                    class="p-4 text-start font-normal cursor-pointer hover:shadow-sm transition duration-200"
                                >
                                    {#if !header.isPlaceholder}
                                        <div class="flex items-center gap-2">
                                            <FlexRender {header} />

                                            {#if header.column.getIsSorted() === "asc"}
                                                <IconSortAscending
                                                    height="1em"
                                                />
                                            {:else if header.column.getIsSorted() === "desc"}
                                                <IconSortDescensing
                                                    height="1em"
                                                />
                                            {:else if header.column.getCanSort()}
                                                <IconArrowsUpDown
                                                    height="1em"
                                                />
                                            {/if}
                                        </div>
                                    {/if}
                                </th>
                            {/each}
                            <th class="p-4 text-start">
                                <IconFilter height="1.3em" class="shrink-0" />
                            </th>
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

                            <td class="p-4 py-4 text-start">
                                <IconDotsVertical
                                    height="1em"
                                    class="shrink-0"
                                />
                            </td>
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
