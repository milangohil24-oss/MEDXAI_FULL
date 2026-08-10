import {createContext,useContext,useEffect,useState} from 'react';import type {ReactNode} from 'react';import type {User} from '../types';import {api} from '../services/api';
type Auth={user:User|null;loading:boolean;login:(e:string,p:string)=>Promise<void>;register:(n:string,e:string,p:string)=>Promise<void>;logout:()=>Promise<void>};
const C=createContext<Auth|null>(null);
function extractToken(x:any){return x?.access_token||x?.token||x?.accessToken||x?.data?.access_token}
export function AuthProvider({children}:{children:ReactNode}){const [user,setUser]=useState<User|null>(null),[loading,setLoading]=useState(true);
 useEffect(()=>{if(localStorage.getItem('medxai_token')) api.me().then(setUser).catch(()=>localStorage.removeItem('medxai_token')).finally(()=>setLoading(false));else setLoading(false)},[]);
 const login=async(e:string,p:string)=>{const x=await api.login({email:e,password:p});const t=extractToken(x);if(!t)throw Error('Login succeeded but the backend did not return a JWT access token.');localStorage.setItem('medxai_token',t);setUser(await api.me())};
 const register=async(n:string,e:string,p:string)=>{await api.register({name:n,email:e,password:p});await login(e,p)};
 const logout=async()=>{try{await api.logout()}catch{}localStorage.removeItem('medxai_token');setUser(null)};
 return <C.Provider value={{user,loading,login,register,logout}}>{children}</C.Provider>}
export const useAuth=()=>{const x=useContext(C);if(!x)throw Error('AuthProvider missing');return x};
