import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { DocsLayout } from '@/layouts/DocsLayout'
import { HomePage } from '@/pages/HomePage'
import { DocPage } from '@/pages/DocPage'
import { NotFoundPage } from '@/pages/NotFoundPage'

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route element={<DocsLayout />}>
          <Route path="/docs/:topic/:slug" element={<DocPage />} />
        </Route>
        <Route path="*" element={<NotFoundPage />} />
      </Routes>
    </BrowserRouter>
  )
}
