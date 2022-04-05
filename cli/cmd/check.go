package cmd

import (
	"os"
	"os/exec"

	"github.com/apex/log"
	"github.com/spf13/cobra"
	"github.com/tarantool/tt/cli/cmdcontext"
	"github.com/tarantool/tt/cli/modules"
	"github.com/tarantool/tt/cli/running"
)

// NewCheckCmd creates a new ckeck command.
func NewCheckCmd() *cobra.Command {
	var checkCmd = &cobra.Command{
		Use:   "check [APPLICATION_NAME]",
		Short: "Check an application file for syntax errors",
		Run: func(cmd *cobra.Command, args []string) {
			err := modules.RunCmd(&cmdCtx, cmd.Name(), &modulesInfo, internalCheckModule, args)
			if err != nil {
				log.Fatalf(err.Error())
			}
		},
	}

	return checkCmd
}

// internalCheckModule is a default check module.
func internalCheckModule(cmdCtx *cmdcontext.CmdCtx, args []string) error {
	cliOpts, err := modules.GetCliOpts(cmdCtx.Cli.ConfigPath)
	if err != nil {
		return err
	}

	if err = running.FillCtx(cliOpts, cmdCtx, args); err != nil {
		return err
	}

	os.Setenv("TT_CLI_INSTANCE", args[0])
	cmd := exec.Command(cmdCtx.Cli.TarantoolExecutable, "-e", running.CheckSyntax)
	stdout, err := cmd.Output()
	if err != nil {
		log.Fatalf("Problem with exec lua check function code via tarantool -e: %s", err.Error())
		return nil
	}
	log.Info(string(stdout))
	return nil
}
