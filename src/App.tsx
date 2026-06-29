import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { SearchUIProvider } from '@/contexts/SearchUIContext'
import { DocsLayout } from '@/layouts/DocsLayout'
import { HomePage } from '@/pages/HomePage'
import { DocPage } from '@/pages/DocPage'
import { DocsIndexPage } from '@/pages/DocsIndexPage'
import { DashboardPage } from '@/pages/DashboardPage'
import { NotFoundPage } from '@/pages/NotFoundPage'

export default function App() {
  return (
    <BrowserRouter>
      <SearchUIProvider>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route element={<DocsLayout />}>
          <Route path="/docs" element={<DocsIndexPage />} />
          <Route path="/docs/:topic/:slug" element={<DocPage />} />
          <Route path="/dashboard" element={<DashboardPage />} />
        </Route>
        <Route path="*" element={<NotFoundPage />} />
      </Routes>
      </SearchUIProvider>
    </BrowserRouter>
  )
}
