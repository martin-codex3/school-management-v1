<script lang="ts">
    import type { BranchData } from "#lib/types/branches/branch_data.ts";
    import {
        createTable,
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
            accessorKey: "city",
            header: "City",
        },

        {
            accessorKey: "nationality",
            header: "Nationality",
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

<div class="h-screen overflow-hidden flex items-center justify-center">
    <div class="h-[calc(100vh-2rem)] overflow-hidden bg-white rounded-4xl">
        <!-- for the main table controllers -->
        <div class="h-full overflow-auto scrollbar-none">
            <!-- for the table header -->
            <div class="">
                <h1>hey</h1>
            </div>

            <!-- for the table body -->
            <div class="">
                <h1>table body</h1>
            </div>

            <!-- for the table footer -->
            <div class="">
                <h1>table footer</h1>
            </div>
        </div>
    </div>
</div>
