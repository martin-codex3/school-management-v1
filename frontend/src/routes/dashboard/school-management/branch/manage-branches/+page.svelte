<script lang="ts">
    import {
        createTable,
        tableFeatures,
        columnVisibilityFeature,
    } from "@tanstack/svelte-table";
    import type { ColumnDef } from "@tanstack/svelte-table";
    import type { PageProps } from "./$types";
    import { FlexRender } from "@tanstack/svelte-table";
    import type { BranchResponse } from "#lib/types/branches/branch.ts";
    import DotsIcon from "@iconify-svelte/tabler/dots-vertical";

    const { data }: PageProps = $props();

    // for the tanstack table here
    const features = tableFeatures({ columnVisibilityFeature });

    const columns: ColumnDef<typeof features, BranchResponse>[] = [
        { accessorKey: "branch_name", header: "Branch Name" },
        { accessorKey: "branch_email", header: "Branch Email" },
        { accessorKey: "address_line_1", header: "Address Line 1" },
        { accessorKey: "city", header: "City" },
        { accessorKey: "nationality", header: "Nationality" },
    ];

    const table = createTable({
        features,
        columns,
        get data() {
            return data.branches;
        },
    });

    // for click events on the rows
    const handleClickRow = (rowId: string) => {
        const row = table.getRow(rowId);
        console.log(row.original);
    };
</script>

<div class="h-screen overflow-hidden flex items-center justify-center">
    <div
        class="h-[calc(100vh-1rem)] bg-white border w-full border-gray-300 rounded-4xl"
    >
        <div class="h-full overflow-auto scrollbar-thin space-y-10">
            <!-- for the table header -->
            <div class="px-5 py-5">
                <h1 class="text-xl capitalize font-semibold">
                    manage branches
                </h1>
                <p>
                    Manage all branch data. click on the row to access more
                    options.
                </p>
            </div>

            <div class="">
                <table class="w-full table-auto border-collapse">
                    <thead>
                        {#each table.getHeaderGroups() as headerGroup (headerGroup.id)}
                            <tr class="bg-purple-50 text-purple-950">
                                {#each headerGroup.headers as header}
                                    <th
                                        class="text-sm text-start p-4 border-b border-b-gray-200"
                                    >
                                        {#if !header.isPlaceholder}
                                            <FlexRender {header} />
                                        {/if}
                                    </th>
                                {/each}

                                <th
                                    class="text-sm text-start p-4 border-b border-b-gray-200"
                                ></th>
                            </tr>
                        {/each}
                    </thead>

                    <tbody>
                        {#each table.getRowModel().rows as row (row.id)}
                            <tr
                                onclick={() => handleClickRow(row.id)}
                                class="odd:bg-white even:bg-gray-100 cursor-pointer hover:bg-gray-50 transition duration-200"
                            >
                                {#each row.getAllCells() as cell (cell.id)}
                                    <td
                                        class="text-sm border-b border-b-gray-200 text-start p-4"
                                    >
                                        <FlexRender {cell} />
                                    </td>
                                {/each}

                                <td
                                    class="text-sm border-b border-b-gray-200 text-start p-4"
                                >
                                    <h1>hey</h1>
                                </td>
                            </tr>
                        {/each}

                        {#if table.getRowModel().rows.length === 0}
                            <tr>
                                <td>
                                    <div
                                        class="h-full flex items-center justify-center"
                                    >
                                        <h1>no available records</h1>
                                    </div>
                                </td>
                            </tr>
                        {/if}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
