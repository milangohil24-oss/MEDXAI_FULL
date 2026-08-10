import type {Analysis,DashboardStats,Prediction,User} from '../types';
export const API=import.meta.env.VITE_API_BASE_URL||'http://127.0.0.1:8000';
const token=()=>localStorage.getItem('medxai_token');
async function request<T>(path:string,init:RequestInit={},auth=true):Promise<T>{
 const headers=new Headers(init.headers); if(!(init.body instanceof FormData)) headers.set('Content-Type','application/json'); if(auth&&token()) headers.set('Authorization',`Bearer ${token()}`);
 const r=await fetch(`${API}${path}`,{...init,headers}); const text=await r.text(); let data:any; try{data=text?JSON.parse(text):null}catch{data=text}
 if(!r.ok) throw new Error(data?.detail||data?.message||`Request failed (${r.status})`); return data as T;
}
export const api={
 async register(payload:{name:string;email:string;password:string}){return request<any>('/auth/register',{method:'POST',body:JSON.stringify(payload)},false)},
 async login(payload:{email:string;password:string}){return request<any>('/auth/login',{method:'POST',body:JSON.stringify(payload)},false)},
 me:()=>request<User>('/auth/me'),
 logout:()=>request<any>('/auth/logout',{method:'POST'}),
 predict:(file:File)=>{const f=new FormData();f.append('file',file);return request<Prediction>('/predict',{method:'POST',body:f})},
 analyses:()=>request<Analysis[]>('/analyses'),
 analysis:(id:string)=>request<Analysis>(`/analyses/${id}`),
 deleteAnalysis:(id:string)=>request<any>(`/analyses/${id}`,{method:'DELETE'}),
 stats:()=>request<DashboardStats>('/dashboard/stats'),
 profile:()=>request<User>('/profile'),
 updateProfile:(p:Partial<User>)=>request<User>('/profile',{method:'PUT',body:JSON.stringify(p)}),
 changePassword:(p:{current_password:string;new_password:string})=>request<any>('/auth/change-password',{method:'POST',body:JSON.stringify(p)}),
 reports:()=>request<any[]>('/reports'),
 createReport:(id:string)=>request<any>(`/reports/${id}`,{method:'POST'}),
 lime:(id:string)=>request<any>(`/explain/lime`,{method:'POST',body:JSON.stringify({analysis_id:id})}),
 imageUrl:(url?:string)=>!url?'':url.startsWith('http')?url:`${API}${url.startsWith('/')?'':'/'}${url}`,
 reportUrl:(id:string)=>`${API}/reports/${id}/download`,
};
