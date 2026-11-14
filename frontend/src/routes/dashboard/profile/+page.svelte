<script lang="ts">
    import type { PageProps } from "../$types";

    let { data }: PageProps = $props();
</script>

<div class="">
    <div class="h-screen flex items-center justify-center">
        <div
            class="bg-white rounded-4xl w-full max-w-3xl h-[calc(100vh-2rem)] space-y-10 mx-auto px-10 py-5"
        >
            <!-- for the main header -->
            <div
                class="flex items-center gap-3 w-full border border-gray-300 bg-gray-50 rounded-full px-2 py-2"
            >
                <div class="h-20 w-20 rounded-full bg-purple-400"></div>
                <div>
                    <h1 class="text-lg capitalize font-semibold">
                        {data.user.first_name}
                    </h1>
                    <p>{data.user.email}</p>
                </div>
            </div>

            <!-- for the main content here -->
            <div class="">
                <div
                    class="rounded-tr-3xl rounded-tl-3xl flex items-center justify-between px-5 py-2 rounded-bl-lg rounded-br-lg bg-gray-100"
                >
                    <div class="flex items-center gap-5">
                        <div>
                            <h1>icon</h1>
                        </div>

                        <div>
                            <h1>First name</h1>
                            <p>The name associated with your account</p>
                        </div>
                    </div>

                    <div>
                        <h2>{data.user.first_name}</h2>
                        <button
                            aria-label="open update modal"
                            title="Open Update Modal"
                        >
                            <span>open</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
