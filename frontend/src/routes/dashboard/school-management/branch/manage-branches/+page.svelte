<script lang="ts">
    import {
        createTable,
        tableFeatures,
        columnVisibilityFeature,
    } from "@tanstack/svelte-table";
    import type { ColumnDef } from "@tanstack/svelte-table";
    import type { PageProps } from "./$types";
    import type { SchoolBranches } from "#lib/types/branches/school_braches.ts";
    import { FlexRender } from "@tanstack/svelte-table";
    import type { BranchResponse } from "#lib/types/branches/branch.ts";

    const { data }: PageProps = $props();

    // for the tanstack table here
    const features = tableFeatures({ columnVisibilityFeature });

    const columns: ColumnDef<typeof features, SchoolBranches>[] = [
        { accessorKey: "branch_name", header: "Branch Name" },
        { accessorKey: "branch_email", header: "Branch Email" },
        { accessorKey: "branch_phone", header: "Branch Phone" },
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
    const handleClickRow = () => {
        const row = table.getRowModel;
        console.log(row);
        console.log("We are clicking this row");
    };

    $effect(() => {
        console.log(table.getRowModel().rows);
    });
</script>

<div class="h-screen overflow-hidden flex items-center justify-center">
    <div
        class="h-[calc(100vh-1rem)] bg-white border w-full border-gray-300 rounded-4xl"
    >
        <div class="h-full overflow-auto scrollbar-thin">
            <!-- for the table header -->
            <div class="px-5 py-3">
                <h1 class="text-xl capitalize font-semibold">
                    manage branches
                </h1>
                <p>
                    Manage all branch data. click on the row to access more
                    options.
                </p>
            </div>

            <div>
                <table class="w-full table-auto border-collapse">
                    <thead>
                        {#each table.getHeaderGroups() as headerGroup (headerGroup.id)}
                            <tr>
                                {#each headerGroup.headers as header}
                                    <th class="text-sm text-start">
                                        {#if !header.isPlaceholder}
                                            <FlexRender {header} />
                                        {/if}
                                    </th>
                                {/each}
                            </tr>
                        {/each}
                    </thead>

                    <tbody>
                        {#each table.getRowModel().rows as row (row.id)}
                            <tr>
                                {#each row.getAllCells() as cell (cell.id)}
                                    <td>
                                        <FlexRender {cell} />
                                    </td>
                                {/each}
                            </tr>
                        {/each}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
