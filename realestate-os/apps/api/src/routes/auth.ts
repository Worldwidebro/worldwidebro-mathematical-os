import express from 'express';
import { supabase } from '../index';

const router = express.Router();

router.post('/register', async (req, res) => {
  const { email, password, fullName, role } = req.body;

  try {
    const { data: authData, error: authError } = await supabase.auth.admin.createUser({
      email,
      password,
      email_confirm: true,
    });

    if (authError) throw authError;

    await supabase.from('users').insert({
      id: authData.user.id,
      email,
      full_name: fullName,
      role,
    });

    res.json({ userId: authData.user.id });
  } catch (err) {
    res.status(400).json({ error: String(err) });
  }
});

router.post('/login', async (req, res) => {
  const { email, password } = req.body;

  try {
    const { data, error } = await supabase.auth.signInWithPassword({
      email,
      password,
    });

    if (error) throw error;

    res.json({
      accessToken: data.session.access_token,
      refreshToken: data.session.refresh_token,
      user: data.user,
    });
  } catch (err) {
    res.status(401).json({ error: String(err) });
  }
});

export default router;
