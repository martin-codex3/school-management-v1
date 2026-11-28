<script lang="ts">
    import { tableFeatures, type ColumnDef } from "@tanstack/svelte-table";

    // we will get all the table functionalities here
    interface Branch {
        branch_name: string;
        branch_email: string;
        branch_phone: string;
        city: string;
        nationality: string;
        district: string;
    }

    // tables features
    const features = tableFeatures({});

    // table columns
    const columns: ColumnDef<typeof features, Branch>[] = [
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
</script>

<div>
    <h1>we will start here</h1>
</div>
