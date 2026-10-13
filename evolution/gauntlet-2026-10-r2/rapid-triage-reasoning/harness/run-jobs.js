export const meta = {
  name: 'gauntlet-run-jobs',
  description: 'Run gauntlet prompt-file jobs (executors or instruments); each agent writes its own output file and returns one line',
  phases: [{ title: 'Run', detail: 'one agent per job; outputs go to files, never to this context' }],
}

// args: { run: <absolute round dir>, jobs: [{ id, prompt (relative to run), model, effort }] }
const DONE = { type: 'object', properties: { status: { type: 'string' } }, required: ['status'] }

phase('Run')
const results = await pipeline(args.jobs, (job) =>
  agent(`Read ${args.run}/${job.prompt} and do exactly what it says. Return only: done`,
    { label: job.id, phase: 'Run', model: job.model, effort: job.effort, agentType: job.agent, schema: DONE })
    .then((r) => ({ id: job.id, ok: !!r })))

const failed = args.jobs.map((j, i) => (results[i] && results[i].ok ? null : j.id)).filter(Boolean)
log(`done ${args.jobs.length - failed.length}/${args.jobs.length}`)
return { done: args.jobs.length - failed.length, failed }
