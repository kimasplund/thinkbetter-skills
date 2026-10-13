export const meta = {
  name: 'uplift-run-batch',
  description: 'Run Haiku-uplift prompt-file jobs across rounds; each agent writes its own output file and returns one line',
  phases: [{ title: 'Run', detail: 'one gauntlet-worker per job; outputs go to files, never to this context' }],
}

// args: { run: <program root>, jobs: [[prompt path relative to run, model, effort], ...] }
const DONE = { type: 'object', properties: { status: { type: 'string' } }, required: ['status'] }

phase('Run')
const results = await pipeline(args.jobs, ([prompt, model, effort]) =>
  agent(`Read ${args.run}/${prompt} and do exactly what it says. Return only: done`,
    { label: prompt.replace(/\/jobs\/(exec|judge)\//, ':').replace(/\.md$/, ''), phase: 'Run', model, effort,
      agentType: 'gauntlet-worker', schema: DONE })
    .then((r) => ({ prompt, ok: !!r })))

const failed = args.jobs.map((j, i) => (results[i] && results[i].ok ? null : j[0])).filter(Boolean)
log(`done ${args.jobs.length - failed.length}/${args.jobs.length}`)
return { done: args.jobs.length - failed.length, failed }
