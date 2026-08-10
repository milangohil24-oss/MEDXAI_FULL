export type User={id:string;name:string;email:string;created_at?:string};
export type Prediction={prediction:string;confidence:number;confidence_percentage:number;probabilities:Record<string,number>;gradcam_url?:string;lime_url?:string;filename?:string;analysis_id?:string};
export type Analysis=Prediction & {id:string;created_at:string;filename:string};
export type DashboardStats={total_analyses:number;average_confidence:number;latest_prediction?:string;recent?:Analysis[]};
