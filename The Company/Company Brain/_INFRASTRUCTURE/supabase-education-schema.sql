-- Supabase schema for education/learning platform

-- Courses table
CREATE TABLE IF NOT EXISTS courses (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL,
  title TEXT NOT NULL,
  description TEXT,
  topic TEXT,
  curriculum JSONB,  -- Structured outline
  status TEXT DEFAULT 'draft',  -- draft, published, archived
  created_by TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Classrooms (live course instances)
CREATE TABLE IF NOT EXISTS classrooms (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  course_id UUID REFERENCES courses(id),
  venture_id TEXT NOT NULL,
  name TEXT,
  status TEXT DEFAULT 'draft',  -- draft, ready, live, archived
  start_date TIMESTAMP,
  end_date TIMESTAMP,
  max_students INT DEFAULT 30,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Student enrollments
CREATE TABLE IF NOT EXISTS enrollments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  classroom_id UUID REFERENCES classrooms(id),
  student_id UUID,
  venture_id TEXT NOT NULL,
  status TEXT DEFAULT 'active',  -- active, completed, dropped
  progress DECIMAL DEFAULT 0,  -- 0-100%
  enrolled_at TIMESTAMP DEFAULT NOW(),
  completed_at TIMESTAMP
);

-- Learning progress tracking
CREATE TABLE IF NOT EXISTS learning_progress (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  enrollment_id UUID REFERENCES enrollments(id),
  slide_number INT,
  quiz_score DECIMAL,
  time_spent_seconds INT,
  completed_at TIMESTAMP DEFAULT NOW()
);

-- Quiz results
CREATE TABLE IF NOT EXISTS quiz_results (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  enrollment_id UUID REFERENCES enrollments(id),
  quiz_id TEXT,
  score DECIMAL,
  total_questions INT,
  correct_answers INT,
  completed_at TIMESTAMP DEFAULT NOW()
);

-- Course metrics/outcomes
CREATE TABLE IF NOT EXISTS course_outcomes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  course_id UUID REFERENCES courses(id),
  venture_id TEXT NOT NULL,
  enrollment_count INT DEFAULT 0,
  completion_rate DECIMAL DEFAULT 0,
  average_quiz_score DECIMAL DEFAULT 0,
  average_time_spent_hours DECIMAL DEFAULT 0,
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Slide content
CREATE TABLE IF NOT EXISTS slides (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  course_id UUID REFERENCES courses(id),
  slide_number INT,
  title TEXT,
  content JSONB,  -- Structure: title, bullet_points, speaker_notes
  images JSONB,   -- Array of image URLs
  audio_url TEXT, -- TTS audio
  duration_seconds INT,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Quiz questions
CREATE TABLE IF NOT EXISTS quiz_questions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  course_id UUID REFERENCES courses(id),
  module_number INT,
  question_type TEXT,  -- multiple_choice, true_false, short_answer
  question TEXT,
  options JSONB,       -- For multiple choice
  correct_answer TEXT,
  explanation TEXT,
  difficulty INT,      -- 1-5 scale
  created_at TIMESTAMP DEFAULT NOW()
);

-- Interactive elements
CREATE TABLE IF NOT EXISTS interactive_elements (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  course_id UUID REFERENCES courses(id),
  element_type TEXT,  -- simulation, game, pbl
  title TEXT,
  spec JSONB,         -- Full specification
  created_at TIMESTAMP DEFAULT NOW()
);

-- Exported files
CREATE TABLE IF NOT EXISTS exported_files (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  course_id UUID REFERENCES courses(id),
  venture_id TEXT NOT NULL,
  file_type TEXT,     -- pptx, html, pdf, zip
  file_url TEXT,
  file_size_bytes INT,
  exported_at TIMESTAMP DEFAULT NOW()
);

-- Enable RLS
ALTER TABLE courses ENABLE ROW LEVEL SECURITY;
ALTER TABLE classrooms ENABLE ROW LEVEL SECURITY;
ALTER TABLE enrollments ENABLE ROW LEVEL SECURITY;
ALTER TABLE learning_progress ENABLE ROW LEVEL SECURITY;
ALTER TABLE quiz_results ENABLE ROW LEVEL SECURITY;
ALTER TABLE course_outcomes ENABLE ROW LEVEL SECURITY;

-- RLS Policies (students can only see their own progress)
CREATE POLICY "Students can view their own enrollments"
  ON enrollments FOR SELECT
  USING (auth.uid()::text = student_id::text);

CREATE POLICY "Students can view their own progress"
  ON learning_progress FOR SELECT
  USING (
    auth.uid()::text IN (
      SELECT student_id::text FROM enrollments
      WHERE id = enrollment_id
    )
  );

CREATE POLICY "Students can view their quiz results"
  ON quiz_results FOR SELECT
  USING (
    auth.uid()::text IN (
      SELECT student_id::text FROM enrollments
      WHERE id = enrollment_id
    )
  );

-- Indexes for performance
CREATE INDEX idx_courses_venture ON courses(venture_id);
CREATE INDEX idx_classrooms_course ON classrooms(course_id);
CREATE INDEX idx_enrollments_classroom ON enrollments(classroom_id);
CREATE INDEX idx_enrollments_student ON enrollments(student_id);
CREATE INDEX idx_learning_progress_enrollment ON learning_progress(enrollment_id);
CREATE INDEX idx_quiz_results_enrollment ON quiz_results(enrollment_id);
CREATE INDEX idx_slides_course ON slides(course_id);
CREATE INDEX idx_quiz_questions_course ON quiz_questions(course_id);
