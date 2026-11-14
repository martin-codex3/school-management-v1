export interface UserResponse {
    id: string,
    first_name: string,
    last_name: string,
    email: string,
    phone_number: string,
    bio: string | null,
    profile_image_url: string | null
}