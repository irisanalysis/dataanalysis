export default function Home() {
  return (
    <main className="min-h-screen p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold text-center mb-8">
          Next.js + FastAPI Application
        </h1>
        <div className="bg-white rounded-lg shadow-md p-6">
          <h2 className="text-2xl font-semibold mb-4">Welcome to your development environment</h2>
          <p className="text-gray-600 mb-4">
            This is a full-stack application with Next.js frontend and FastAPI backend,
            connected to a PostgreSQL database with vector support.
          </p>
          <div className="space-y-4">
            <div className="p-4 bg-blue-50 rounded">
              <h3 className="font-semibold text-blue-800">Frontend</h3>
              <p className="text-blue-600">Next.js 14 with TypeScript</p>
            </div>
            <div className="p-4 bg-green-50 rounded">
              <h3 className="font-semibold text-green-800">Backend</h3>
              <p className="text-green-600">FastAPI with Python</p>
            </div>
            <div className="p-4 bg-purple-50 rounded">
              <h3 className="font-semibold text-purple-800">Database</h3>
              <p className="text-purple-600">PostgreSQL with vector extension</p>
            </div>
          </div>
        </div>
      </div>
    </main>
  )
}