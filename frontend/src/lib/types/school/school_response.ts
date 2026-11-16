export interface SchoolResponse {
    id: string;
    school_name: string
    school_type: string
    school_email: string
    school_phone: string
    address: string
    city: string
    country: string
    website_url: string | undefined
    registration_number: string | undefined
    school_code: string | undefined
    description: string | undefined
    settings: object
}