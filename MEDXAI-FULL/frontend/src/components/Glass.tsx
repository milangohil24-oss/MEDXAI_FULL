import type { ReactNode } from "react";

interface GlassProps {
  children: ReactNode;
  className?: string;
}

export function Glass({ children, className = "" }: GlassProps) {
  return (
    <div className={`glass-panel ${className}`}>
      {children}
    </div>
  );
}

export default Glass;
