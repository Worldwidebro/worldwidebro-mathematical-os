'use client';
import { styles } from '@/styles/tokens';
export default function Utickets() {
  return <div style={styles.container as React.CSSProperties}><h1>tickets</h1><div style={styles.card as React.CSSProperties}><button style={styles.primaryButton as React.CSSProperties}>Manage</button></div></div>;
}
